html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Info Table</title>
    <style>
        table {
            width: 50%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 10px;
            text-align: center;
        }
    </style>
</head>
<body>
<nav>
    <a href="index.html">Home</a>
    <a href="ethics.html">Ethics</a>
    <a href="contact.html">Contact</a>
</nav>

<h2>My Introduction Table</h2>

<table>
    <tr>
        <td><strong>Name</strong></td>
        <td>Hugo Monjes</td>
    </tr>
    <tr>
        <td><strong>Introduction</strong></td>
        <td>Hello, I am a junior in the BS IT program. I enjoy learning more about Python.</td>
    </tr>
    <tr>
        <td><strong>Hobbies</strong></td>
        <td>Some of my hobbies are cooking, playing sports, and programming.</td>
    </tr>
</table>

</body>
</html>
"""

with open("index.html", "w") as file:
    file.write(html_content)