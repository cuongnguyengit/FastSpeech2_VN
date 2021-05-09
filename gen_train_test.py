import argparse
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--val_path", type=str, help="path to val path")
    parser.add_argument("--outdir", type=str, help="path to val path")
    args = parser.parse_args()

    list_for_val = []

    with open(args.val_path, 'r', encoding='utf-8') as rf:
        lines = rf.read().split('\n')
        for line in lines:
            name = str(line.split('|')[0]).split('/')[-1][:-4]
            list_for_val.append(name)


    with open(os.path.join(args.outdir, 'train.txt'), 'w', encoding='utf-8') as tw, open(os.path.join(args.outdir, 'val.txt'), 'w', encoding='utf-8') as vw:
        with open(os.path.join(args.outdir, 'full.txt'), 'r', encoding='utf-8') as rf:
            lines = rf.read().split('\n')
            for line in lines:
                name = line.split('|')[0]
                if name in list_for_val:
                    vw.write(line + '\n')
                else:
                    tw.write(line + '\n')