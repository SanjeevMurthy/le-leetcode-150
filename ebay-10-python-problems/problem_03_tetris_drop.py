"""
Problem 3: Tetris Drop / Figure on a Field (Q3)
Slot: Q3 (implementation-heavy 2D) | Probability: 20-35% (isomorph)

Given a 2D field (grid of 0s and 1s) and a figure (smaller 2D grid of 0s and 1s
with the same number of columns as the field), drop the figure from the top.
The figure falls until it would overlap an existing 1 in the field, or reach the bottom.
Return the resulting field after the figure lands.

The figure is left-aligned with the field (column 0 of figure = column 0 of field).

Strategy (column-by-column drop calculation):
  For each column c in the figure:
    - Find the lowest non-zero row in the figure for column c  (fig_bottom)
    - Find the topmost non-zero row in the field for column c  (field_top)
    - Max drop allowed by this column = field_top - fig_bottom - 1
  Take the minimum across all columns -> that is the safe drop offset.
  Then place the figure at that offset.

Pattern: Pure 2D grid simulation — write correct boring code fast.
LeetCode equivalents: 73, 48, 36, 794, 419, 1861
"""


def solution(field: list[list[int]], figure: list[list[int]]) -> list[list[int]]:
    rows = len(field)
    cols = len(field[0])
    fig_rows = len(figure)
    fig_cols = len(figure[0])

    drop = rows  # start with maximum possible drop

    for col in range(fig_cols):
        # Lowest occupied row in figure for this column
        fig_bottom = -1
        for row in range(fig_rows - 1, -1, -1):
            if figure[row][col] != 0:
                fig_bottom = row
                break

        if fig_bottom == -1:
            continue  # column is empty in figure

        # Topmost occupied row in field for this column
        field_top = rows  # default: field column is empty
        for row in range(rows):
            if field[row][col] != 0:
                field_top = row
                break

        # After dropping by `drop`, figure[fig_bottom][col] lands at drop + fig_bottom.
        # That cell must be strictly above field_top:  drop + fig_bottom < field_top
        max_drop = field_top - fig_bottom - 1
        drop = min(drop, max_drop)

    # Place figure into a deep copy of field at the calculated drop offset
    result = [row[:] for row in field]
    for r in range(fig_rows):
        for c in range(fig_cols):
            if figure[r][c] != 0:
                result[drop + r][c] = figure[r][c]

    return result


def _print_grid(grid: list[list[int]]) -> None:
    for row in grid:
        print(" ".join(str(x) for x in row))
    print()


if __name__ == "__main__":
    # Test 1: simple drop to bottom
    field1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [1, 0, 0],
    ]
    figure1 = [
        [1, 1, 0],
        [0, 1, 0],
    ]
    # col0: fig_bottom=0, field_top=3 -> max_drop=2
    # col1: fig_bottom=1, field_top=4 -> max_drop=2  => drop=2
    # figure[0]=[1,1,0] at row2; figure[1]=[0,1,0] at row3 (+existing [1,0,0])
    expected1 = [
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0],
    ]
    result1 = solution(field1, figure1)
    print("[Test 1] Figure drops and aligns above existing block:")
    _print_grid(result1)
    assert result1 == expected1, f"FAIL: got {result1}"
    print("PASS\n")

    # Test 2: figure drops to bottom on empty field
    field2 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    figure2 = [
        [0, 1, 0],
        [1, 1, 1],
    ]
    expected2 = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]
    result2 = solution(field2, figure2)
    print("[Test 2] Figure drops to bottom of empty field:")
    _print_grid(result2)
    assert result2 == expected2, f"FAIL: got {result2}"
    print("PASS\n")

    # Test 3: T-shape piece, uneven column depths
    field3 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]
    figure3 = [
        [1, 1, 1],
    ]
    # col0: fig_bottom=0, field_top=3 -> max_drop=2
    # col1: fig_bottom=0, field_top=1 -> max_drop=0
    # col2: fig_bottom=0, field_top=3 -> max_drop=2
    # drop = 0
    expected3 = [
        [1, 1, 1],
        [0, 1, 0],
        [0, 1, 0],
    ]
    result3 = solution(field3, figure3)
    print("[Test 3] Figure sits on top of tallest column:")
    _print_grid(result3)
    assert result3 == expected3, f"FAIL: got {result3}"
    print("PASS\n")
