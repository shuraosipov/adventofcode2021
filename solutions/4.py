incomplete = '[({(<(())[]>[[{[]{<()<>>'
complete = '{([(<{}[<>[]}>{[]{[(<()>'
close_chars = [')',']','}','>']



if not any(c in incomplete for c in close_chars):
    print("ALALA")

