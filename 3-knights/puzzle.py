from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A cant be both at the same tame
    Or(AKnave, AKnight),
    Not(And(AKnave, AKnight)),
    
    # If a is a Knight(doesn't lie) then they are both a knigh and a knave
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # They can't be both at the same time
    Or(AKnave, AKnight),
    Not(And(AKnave, AKnight)),
    Or(BKnave, BKnight),
    Not(And(BKnave, BKnight)),
    # If A told the truth then both are Knaves(A is lying)
    Biconditional(AKnight, And(AKnave, BKnave))
)
# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # They can't be both at the same time
    Or(AKnave, AKnight),
    Not(And(AKnave, AKnight)),
    Or(BKnave, BKnight),
    Not(And(BKnave, BKnight)),
    
    # If A told thetruth then both are the same kind and then A is Knight
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(BKnave, AKnave))),
    # If B told the truth then both are the different kind and then B is Knight
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # They can't be both at the same time
    Or(AKnave, AKnight),
    Not(And(AKnave, AKnight)),
    Or(BKnave, BKnight),
    Not(And(BKnave, BKnight)),
    Or(CKnave, CKnight),
    Not(And(CKnave, CKnight)),
    
    
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    # if B told the then C is a knave
    Biconditional(BKnight, CKnave),
    # if C told the truth then A is a Knight
    Biconditional(CKnight, AKnight)  
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
