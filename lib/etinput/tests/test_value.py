from pathlib import Path
import pytest

from etinput.value import Value


def test_write_to():
    key = 'some_key'
    value = Value(key)

    base_path = Path('tests/').resolve() / 'tmp'
    base_path.mkdir(exist_ok=True)

    new_file = base_path / f'{key}.csv'

    # Write to without value set raises an error
    with pytest.raises(ValueError):
        value.write_to(new_file)

    # Now set the value and it should work
    value.update(3.5)
    value.write_to(new_file)

    assert new_file.exists()

    # Clean up
    new_file.unlink()
