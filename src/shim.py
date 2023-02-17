def table(query_function=None,
          name=None,
          comment=None,
          spark_conf=None,
          table_properties=None,
          partition_cols=None,
          path=None,
          schema=None,
          temporary=False):
    return _expect(query_function)


def view(query_function=None, name=None, comment=None, spark_conf=None): return _expect(query_function)


def create_streaming_live_table(name, comment=None, spark_conf=None, table_properties=None, partition_cols=None, path=None, schema=None): return None


def read(name): return None


def read_stream(name): return None


def expect(name, inv): return _expect([name, inv])


def expect_or_fail(name, inv): return _expect([name, inv])


def expect_or_drop(expectations): return _expect(expectations)


def expect_all_or_fail(expectations): return _expect(expectations)


def expect_all_or_drop(expectations): return _expect(expectations)


def expect_all(expectations): return _expect(expectations)


def apply_changes(target,
                  source,
                  keys,
                  sequence_by,
                  where=None,
                  ignore_null_updates=False,
                  apply_as_deletes=None,
                  apply_as_truncates=None,
                  column_list=None,
                  except_column_list=None,
                  stored_as_scd_type="1",
                  track_history_column_list=None,
                  track_history_except_column_list=None):
    return None


create_view = view
create_table = table
create_streaming_table = create_streaming_live_table
create_target_table = create_streaming_live_table


def _expect(expectations):
    def outer(func):
        return func

    return outer
