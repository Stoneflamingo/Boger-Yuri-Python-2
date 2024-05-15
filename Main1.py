import Start
import argparse

parser = argparse.ArgumentParser(description="Choosing a type of generate\n")
parser.add_argument("-s", "--strings", default=10, help="number of lines\n")
parser.add_argument("-c", "--columns", default=10, help="number of columns\n")
parser.add_argument("-t", "--type", default=0, help="type of generate,\n 0 -> Create in game"
                                                    "\n 1 -> DFS,\n 2 -> Tree Generate")
args = parser.parse_args()

fl = (int(args.type) == 0)
st = Start.Game(int(args.strings), int(args.columns), int(args.type))
st.prev_game()
