class Piece:
    def __init__(self, name, composer, key):
        self.name = name
        self.composer = composer
        self.key = key


pieces = []

n = int(input())

for _ in range(n):
    name, composer, key = input().split("|")
    piece = Piece(name, composer, key)
    pieces.append(piece)

data = input()
while not data == "Stop":
    split_data = data.split("|")
    if split_data[0] == "Add":
        piece, composer, key = split_data[1:]
        all_names = [p.name for p in pieces]
        if piece in all_names:
            print(f"{piece} is already in the collection!")
        else:
            new_piece = Piece(piece, composer, key)
            pieces.append(new_piece)
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif split_data[0] == "Remove":
        piece = split_data[1]
        all_names = [p.name for p in pieces]
        if piece in all_names:
            piece_to_remove = [p for p in pieces if p.name == piece][0]
            pieces.remove(piece_to_remove)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif split_data[0] == "ChangeKey":
        piece, new_key = split_data[1:]
        all_names = [p.name for p in pieces]
        if piece in all_names:
            piece_to_change = [p for p in pieces if p.name == piece][0]
            piece_to_change.key = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    data = input()

sorted_pieces = sorted(pieces, key=lambda p: (p.name, p.composer))

for piece in sorted_pieces:
    print(f"{piece.name} -> Composer: {piece.composer}, Key: {piece.key}")