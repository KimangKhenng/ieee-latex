import io
import glob

# ここで記載した対をフォーマットする
REPLACE_TEXTS = [
    ['、', '，'],
    ['。', '．'],
    ['１', '1'],
    ['２', '2'],
    ['３', '3'],
    ['４', '4'],
    ['５', '5'],
    ['６', '6'],
    ['７', '7'],
    ['８', '8'],
    ['９', '9'],
    ['０', '0'],
    ['1つ', '一つ'],
    ['2つ', '二つ'],
    ['3つ', '三つ'],
    ['4つ', '四つ'],
    ['5つ', '五つ'],
    ['行なう', '行う'],
    ['様な', 'ような'],
    ['出来', 'でき'],
]


def main():
    files = glob.glob('./**/*.tex', recursive=True)

    replace_texts = REPLACE_TEXTS

    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                s = f.read()

            for replace_text in replace_texts:
                s = s.replace(replace_text[0], replace_text[1])

            with open(file, 'w', encoding='utf-8') as f:
                f.write(s)

        except io.UnsupportedOperation as E:
            print(E)
        print('File Formated: {}'.format(file))

    print('Tex File Format End')


if __name__ == '__main__':
    main()
