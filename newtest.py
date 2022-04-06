    @since(2.0)
    def uncacheTable(self, tableName):
        """Removes the specified table from the in-memory cache."""
        self._jcatalog.uncacheTable(tableName)
