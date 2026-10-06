"""Demonstrate five Python string methods."""


def demo_string_methods() -> None:
	text = "  Hello, Python World!  "

	print("Original text:", repr(text))
	print("strip():", repr(text.strip()))
	print("lower():", text.lower())
	print("upper():", text.upper())
	print("replace():", text.replace("Python", "Programming"))
	print("split():", text.split())


if __name__ == "__main__":
	demo_string_methods()
