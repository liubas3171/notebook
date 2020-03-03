import notebook

if __name__ == '__main__':
    print('For example, we chose class Note from notebook.py')
    print('We create object of this class: \nnote1 = notebook.Note("first note, I`m do this just for example.")\n')
    note1 = notebook.Note('first note', 'I`m do this just for example.')

    print('With function isinstance() we check what is this note1:')
    print('>>> isinstance(note1, str)\n', isinstance(note1, str), '\n')
    print('>>> isinstance(note1, int)\n', isinstance(note1, int), '\n')
    print('isinstance(note1, notebook.Note)\n', isinstance(note1, notebook.Note), '\n')
    print('As we can see, note1 is object of class Note.\n')

    print('There are all attributes and methods of this object:')
    for i in note1.__dir__():
        print(i)
    print('Attribute it is a variable that belongs to object.')
    print('note1 has attributes "memo", "tags", "creation_date", "id"')
    print('>>> note1.memo\n', note1.memo, '\n')
    print('>>> note1.tags\n', note1.tags, '\n')
    print('>>> note1.creation_date\n', note1.creation_date, '\n')
    print('>>> note1.id\n', note1.id, '\n')

    print('A method in python is somewhat similar to a function, except it is associated with object/classes.')
    print('For example, when we do: \n>>> note1 = notebook.Note("first note, I`m do this just for example.")\n'
          'method __init__() makes that we can access attributes of note1 with "." e.g.')
    print('>>> note1.tags\n', note1.tags, '\n')
    print('Other methods can do other things with our object.')
