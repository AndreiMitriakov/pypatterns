#!/usr/bin/env python3
# coding: utf-8

class EditorMemento:

    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content

class Editor:
    
    def __init__(self):
        self.content = ''

    def type(self, words):
        self.content = ' '.join([self.content, words])

    def get_content(self):
        return self.content

    def save(self):
        return EditorMemento(self.content)


    def restore(self, memento):
        self.content = memento.get_content()

if __name__ == '__main__':
    editor = Editor()
    editor.type('ABC')
    editor.type('DEF')
    saved = editor.save()
    editor.type('GHJ')
    print(editor.get_content())
    editor.restore(saved)
    print(editor.get_content())
