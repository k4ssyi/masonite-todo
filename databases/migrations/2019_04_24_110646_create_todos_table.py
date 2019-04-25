from orator.migrations import Migration


class CreateTodosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('todos') as table:
            table.increments('id')
            table.text('body')
            table.integer('status').default(0)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('todos')
