fd_html =  open('index.html', 'r')
html= fd_html.read()

rows = ['<td>%d</td><td>%d</td><td>%d</td>' % (123,456, 789)]

response = html % '\n'.join(rows)
print(response)
