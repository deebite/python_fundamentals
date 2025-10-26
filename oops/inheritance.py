"""
- Python solves diamond problem automatically using C3 Linearization
- Always left-to-right in class declaration (class D(B, C))
- Use ClassName.mro() to verify the order
- If a method exists in multiple parents, the first one in the MRO wins
- Multilevel inheritance → depth first
- Multiple inheritance → left-to-right
- Diamond problem → solved by MRO
"""

class Writer:
    def writer(self):
        print("I am a writer")

class Artist:
    def artist(self):
        print("I am a Artist")


class Multitalent(Writer, Artist):
    def sing(self):
        print("I can sing")

talent = Multitalent();
talent.writer()
talent.artist()
talent.sing()

Multitalent.mro