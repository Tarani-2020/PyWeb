# PyWeb

Are you looking for a simple and easy way to program websites in Python? Then this package is the solution.


## Example

```python
from PyWeb.HTML import *

html = HTML()

h1 = Heading(index=1, content="Das ist ein Titel")
a = Anchor(href="https://wikipedia.org", content="Wikipedia")
p = Paragraph(content="Oder:")
iframe = Iframe("https://wikipedia.org", "", height="500", width="500", loading="lazy")

html.add(h1)
html.add(a)
html.add(p)
html.add(iframe)

html.end()
html.run()
```

### Explanation

```python
from PyWeb.HTML import *
```
- Importing the package
<br>
<br>

```python
html = HTML()
```
- Creating the HTML
<br>
<br>

```python
h1 = Heading(index=1, content="Das ist ein Titel")
a = Anchor(href="https://wikipedia.org", content="Wikipedia")
p = Paragraph(content="Oder:")
iframe = Iframe("https://wikipedia.org", "", height="500", width="500", loading="lazy")
```
- Creating the widgets
<br>
<br>

```python
html.add(h1)
html.add(a)
html.add(p)
html.add(iframe)
```
- Adding the widgets to the HTML
<br>
<br>

```python
html.end()
html.run()
```
- Complete and execute the HTML
