#!/usr/bin/env python3
# coding: utf-8

class BD:
    class __BD:
        def __init__(self):
            self.history = 0

        def info(func):
            def inside(self, *args):
                func(self, *args)
                print('Number of passed operations {}'.format(self.history))
            return inside

        @info
        def query(self, *args):
            for cmd in args:
                self.history += 1
                print('Executing {}'.format(cmd))

    instance = None

    def __new__(self):
        if not BD.instance:
            print('BD is created')
            BD.instance = BD.__BD()
            return BD.instance
        else:
            print('BD is returned')
            return BD.instance

if __name__ == '__main__':
    app1 = BD()
    app1.query('do_smth_1', 'do_smth_2')
    app2 = BD()
    app2.query('do_smth_3')
    
