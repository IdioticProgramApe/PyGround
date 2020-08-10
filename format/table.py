from typing import Any, Iterable


__version__ = "0.1.5"


class Table(object):

    # private variables
    _sep = '='
    _stringstream = ''
    _head = []
    _name = ''
    _alignment = '>'
    _fformat = 'f'
    
    # constructor
    def __init__(self, title: str = None, max_width: int = 6, border: bool = False) -> None:
        super(Table, self).__init__()

        self.border = border
        self._max_width = max_width
        if title:
            self._append(title)

    # private methods
    def _append(self, strline: str, end: str = '\n') -> None:
        self._stringstream += strline
        self._stringstream += end

    def _newl(self) -> None:
        self._stringstream += '\n'

    def _add_separation(self, sep: str) -> None:
        self._append(self._sep * ((len(self._head) - 1) * (self._max_width + len(sep)) + self._max_width))

    # public methods
    def add_head(self, iterable: Iterable[str], sep: str = ' ') -> None:
        if self.border:
            # TODO
            raise NotImplementedError("Current Table doesn't support border")
        else:
            for it in iterable:
                self._head.append(it)

            self.add_line(sep=sep, end='\t')
            self._stringstream += self._name
            self._newl()
            self._add_separation(sep)
    
    def add_line(self, iterable: Iterable[Any] = None, sep: str = ' ', end: str = '\n') -> None:
        if iterable is None:
            iterable = self._head
        
        assert len(iterable) == len(self._head), "Inputs length is incompatible with head info"

        line_string = []
        for it in iterable:
            if isinstance(it, str):
                line_string.append(f"{it:{self._alignment}{self._max_width}}")
            elif isinstance(it, int):
                line_string.append(f"{it:{self._alignment}{self._max_width}d}")
            elif isinstance(it, float):
                line_string.append(f"{it:{self._alignment}{self._max_width}.2{self._fformat}}")
            else:
                raise NotImplementedError(f"{type(it)} not recognizeable")
        
        strline = sep.join(line_string)
        self._append(strline, end)

    def set_name(self, name: str) -> None:
        self._name = name

    def set_width(self, width: int) -> None:
        self._max_width = width

    def set_alignment(self, opt: str) -> None:
        if opt == 'r':
            self._alignment = '>'
        elif opt == 'l':
            self._alignment = '<'
        elif opt == 'c':
            self._alignment = '^'
        else:
            raise RuntimeError("Unknown Alignment Method, choose from ['r', 'l', 'c']")

    def set_float_format(self, _format: str) -> None:
        self._fformat = _format
    
    def clean(self) -> None:
        self._stringstream = ''
        self._head = []
        self._name = ''
    
    # define print stream print(Table) --> self._stringstream
    def __repr__(self) -> str:
        return self._stringstream
    
    # define operator "<<" to add head/line
    def __lshift__(self, iterable: Iterable[Any]) -> object:
        if self._stringstream:
            self.add_line(iterable, sep=' ', end='\n')
        else:
            self.add_head(iterable, sep=' ')
        return self


if __name__ == "__main__":
    # create a table
    table = Table()
    table.set_name("testname.fbx")
    table.set_alignment('r')  # set alignment to 'right'
    table.add_head(["", "a", "b"])
    table.add_line(["c", 5151, 776])
    table.add_line(["d", 0.654646, 0.87989416])
    print("table is below")
    print(table)

    # clean the table to fill in new data
    table.clean()
    print("table is below")
    print(table)

    # new table
    table.set_alignment('c')  # set alignment to 'center'
    table.set_float_format('%')  # this time use percentage
    table.set_width(7)  # since float has extra "%" char, we add one more place to width
    table.add_head(["", "a", "b"])
    table.add_line(["c", 5151, 776])
    table.add_line(["d", 0.654646, 1.0])
    print("table is below")
    print(table)

    # clean again and test operator '<<'
    table.clean()
    table.set_alignment('l')  # set alignment to 'left'
    table.set_float_format('%')  # this time use percentage
    table.set_width(7)  # since float has extra "%" char, we add one more place to width
    table << ["", "a", "b"]
    table << ["c", 5151, 776]
    table << ["d", 0.0, 1.0]
    print("table is below")
    print(table)

    # test chained operator "<<"
    table.clean()
    table.set_alignment('c')  # set alignment to 'left'
    table.set_float_format('f')  # this time use percentage
    table.set_width(6)  # since float has extra "%" char, we add one more place to width
    table << ["", "a", "b"] << ["c", 5151, 776] << ["d", 0.0, 1.0]
    print("table is below")
    print(table)