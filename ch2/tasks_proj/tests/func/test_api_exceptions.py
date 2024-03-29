import pytest
import tasks


class TestUpdate():
    """Test expected exceptions with tasks.update()."""

    @pytest.mark.smoke
    def test_add_raises(self):
        """add() should raise an exception with wrong type param."""
        with pytest.raises(TypeError):
            tasks.add(task='not a Task object')

    @pytest.mark.smoke
    @pytest.mark.get
    def test_start_tasks_db_raises(self):
        """Make sure unsupported db raises an exception."""
        with pytest.raises(ValueError) as excinfo:
            tasks.start_tasks_db('some/great/path', 'mysql')
            exception_msg = excinfo.value.argd[0]
            assert exception_msg == "db_type must be a 'tiny' or 'mongo'"
