---
marp: true
theme: gaia
math: true
---

<!-- _class: lead -->

# `mypy`, but why?

A practical introduction to typing in Python

2023-12-06

Alex Povel

---

## 🚀 you will get an idea of

* ...what typing is all about
  * why is it desirable?
  * how can it solve your problems?
* ...how `mypy` can help you
* ...how `pydantic` can help you

---

## 🌟 about

* samples are Python, but principles are broadly applicable
* some sample code, no live demo
* discussion

---

## 💡 premise

* typing prevents mistakes
  * why? the computer knows better than you (in this case)
* whole error categories disappear
  * ✅ `None.something()` → `AttributeError`
  * ✅ `1 + "2"` → `TypeError` (**we are lucky**)
  * ❌ `1 / 0` → `ZeroDivisionError`
* correction is moved from "run" to "write" time
  * reduces time digging through logs after crashes
  * reduces number of tests needed

---

<!-- _class: lead -->

## `demo()`: wait a minute, fewer tests?

* leverage type system
* make **invalid states** unrepresentable
  * "this `int` is actually a `str`, woops"
* less even remains to test!

---

## 💂‍♀️ guard clauses? no, thanks

* got the basics covered now, what else can we do?

*  

  ```python
  def without_guard(x: int, y: str):
      if x > 420:
          if is_valid_token(y):
              pass  # Code goes here
  ```

* (this relates to *primitive obsession*)

---

```python
def with_guard(x: int, y: str):  # 🤔
    if x <= 420 or not is_valid_token(y):  # Better...
        return

    pass  # Code goes here
```

---

```python
@dataclass
class SomeType:
    x: int
    y: str

    def __post_init__(self):
        pass  # Validation goes here

# Any instance of this type is always guaranteed to be valid, and
# of proper shape.

def no_guard_needed_if_we_never_enter_garbage(st: SomeType):  # ✨
    st.x  # guaranteed to be > 420
    st.y  # guaranteed to be valid token
```

---

<!-- _class: lead -->

## `demo()`: `pydantic`, your code's 👮

* data validation library
* "supercharged" `dataclass`es
* typing is a first-class citizen, great integration
* Rust core 🚀

---

<!-- _class: lead -->

## `demo()`: `pydantic` in a real project

(if there is time)

---

## 🐼 poor `pandas`

* what if everything is a `DataFrame` though?

  ```python
  import pandas as pd

  def double_price(df: pd.DataFrame) -> pd.DataFrame:
      df['Price'] *= 2  # 💥
      return df
  ```

---

* work in progress
  * variadic generics landed in Python 3.11 (PEP 646)
  * new libraries like `static-frame`:

    ```python
    from typing import Any
    from static_frame import Frame, Index, TSeriesAny

    def process(f: Frame[   # type of the container
            Any,            # type of the index labels
            Index[np.str_], # type of the column labels
            np.int_,        # type of the first column
            np.str_,        # type of the second column
            np.float64,     # type of the third column
            ]) -> TSeriesAny: ...
    ```

---

## 😊 conclusion

* use types!
  * they solve world hunger
* use `mypy` to **check for correctness**
  * a good alternative: `pyright`
  * both have IDE integration so they're "fast"
* use `dataclass`es to **structure data** type-friendly
* use `pydantic` to **parse and validate data**
  * important for external, unreliable, untrusted data
* maybe venture out and try typing with `pandas`

---

## 📚 Further reading

* [mypy](https://mypy.readthedocs.io/en/stable/)
* [pyright](https://github.com/microsoft/pyright)
* [pydantic](https://docs.pydantic.dev/latest/)
* [static-frame](https://github.com/static-frame/static-frame)
* [Type-Hinting DataFrames for Static Analysis and Runtime Validation](https://towardsdatascience.com/type-hinting-dataframes-for-static-analysis-and-runtime-validation-3dedd2df481d)
* [PEP 646](https://www.python.org/dev/peps/pep-0646/)
* [PEP 695](https://peps.python.org/pep-0695/)

---

* [Why Type Safety is Important](https://www.shuttle.rs/blog/2023/11/29/type-safety)
* [The type system is a programmer's best friend](https://web.archive.org/web/20230328111411/https://dusted.codes/the-type-system-is-a-programmers-best-friend)
* [How To Survive Your Project's First 100,000 Lines](https://web.archive.org/web/20230505040711/https://verdagon.dev/blog/first-100k-lines)
* [Writing Python like it's Rust](https://kobzol.github.io/rust/python/2023/05/20/writing-python-like-its-rust.html)
* [Make invalid states unrepresentable](https://geeklaunch.io/blog/make-invalid-states-unrepresentable/)
