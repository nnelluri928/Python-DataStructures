#!/usr/bin/env python3

def reverse_s1(s):
	return s[::-1]

print(reverse_s1("Cat"))

def reverse_s2(s):
	res = ''
	for i in range(len(s)):
		res += s[len(s)-1-i]
	return res

print(reverse_s2("hello"))



