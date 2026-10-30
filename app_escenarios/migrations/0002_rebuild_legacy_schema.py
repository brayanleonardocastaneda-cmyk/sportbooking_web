from django.db import migrations


MODEL_NAMES = ('Servicio', 'Escenario', 'ImagenEscenario', 'Resena')


def rebuild_legacy_schema(apps, schema_editor):
    connection = schema_editor.connection
    models = [apps.get_model('app_escenarios', name) for name in MODEL_NAMES]
    models.extend(
        field.remote_field.through
        for model in models[:]
        for field in model._meta.local_many_to_many
    )
    existing_tables = set(connection.introspection.table_names())
    needs_rebuild = False

    for model in models:
        table = model._meta.db_table
        if table not in existing_tables:
            needs_rebuild = True
            break
        with connection.cursor() as cursor:
            columns = {
                column.name
                for column in connection.introspection.get_table_description(cursor, table)
            }
        if any(field.column not in columns for field in model._meta.local_concrete_fields):
            needs_rebuild = True
            break

    if not needs_rebuild:
        return

    for model in reversed(models):
        table = model._meta.db_table
        if table not in existing_tables:
            continue
        backup = f'{table}_legacy'
        suffix = 1
        while backup in existing_tables:
            backup = f'{table}_legacy_{suffix}'
            suffix += 1
        schema_editor.alter_db_table(model, table, backup)
        existing_tables.remove(table)
        existing_tables.add(backup)

    for name in MODEL_NAMES:
        schema_editor.create_model(apps.get_model('app_escenarios', name))


class Migration(migrations.Migration):
    dependencies = [
        ('app_escenarios', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(rebuild_legacy_schema, migrations.RunPython.noop),
    ]
