import pytest
from pathlib import Path

from gopro_renamer.renamer import (
        rename,
        resize_chapter,
        has_ext,
        main
        )


def test_rename(tmp_path):
    old_file = tmp_path / 'foo.mp4'
    old_file.touch()

    new_file = tmp_path / 'bar.mp4'

    rename(old_file, new_file, dryrun=False)

    assert new_file.exists()
    assert not old_file.exists()


def test_rename_dryrun(tmp_path):
    old_file = tmp_path / 'foo.mp4'
    old_file.touch()

    new_file = tmp_path / 'bar.mp4'

    rename(old_file, new_file, dryrun=True)

    assert old_file.exists()
    assert not new_file.exists()


@pytest.mark.parametrize('num, size, new_format, expected', [
    (3, 1, False, '3'),
    (9, 3, False, '009'),
    (5, 2, True, '04')
    ])
def test_resize_chapter(num, size, new_format, expected):
    target = resize_chapter(num, size, new_format)

    assert target == expected


@pytest.mark.parametrize('file, ext, expected', [
    ('path/to/foo.txt', 'txt', True),
    ('bar.csv', 'cs', False),
    ('GO1234.MP4', 'mp4', True),
    ('GO1234.mP4', 'mp4', True),
    ('GO1234.mp4', 'MP4', True),
    ('GO1234.mp4', 'mP4', True),
    ('GO1234.mp4', 'mP4', True),
    ('GO1234.5mp4', 'mP4', False),
    ('GO1234.mp4', '.mP4', True),
    ])
def test_has_ext(file, ext, expected):
    target = has_ext(Path(file), ext)
    assert target == expected







