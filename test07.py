#!/usr/bin/env python3

from day07 import do1, do2, parse, has_color, process
import unittest

'''
'''

DATA = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''.splitlines()

DATA2 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''.splitlines()

class Test1(unittest.TestCase):
    def testParser(self):
        bags = parse(DATA)
        self.assertEqual([], bags['dotted black'] )
        self.assertEqual([(1,'shiny gold')], bags['bright white'] )
        self.assertEqual([(2,'shiny gold'),(9,'faded blue')], bags['muted yellow'] )

    def testProcess(self):
        bags = parse(DATA)
        self.assertTrue(has_color(bags, 'light red'))
        self.assertEqual(4, do1(DATA))

class Test2(unittest.TestCase):
    def test2(self):
        self.assertEqual(32, do2(DATA) )
        self.assertEqual(126, do2(DATA2) )

if __name__=='__main__':
    unittest.main()
