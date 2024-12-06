def main():
    print(create_frame(['midu', 'madeval', 'educalvolpz']))

def create_frame(names):
    width = len(max(names, key=len))
    border = f'{"*" * (width + 4)}'
    frame = [border] + [f'* {name.ljust(width)} *' for name in names] + [border]
    return "\n".join(frame)

if __name__ == "__main__":
    main()