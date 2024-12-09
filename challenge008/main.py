def main():
    print(draw_race([3, 7, -2], 12))


def draw_race(indices, length):
    # Get de pista
    lane = f"{'~'*length}"
    len_indices = len(indices)
    tracks = []
    for i in range(0,len_indices):
        index = indices[i]
        space = len_indices - 1 - i
        index = index if index >= 0 else length + index
        track = lane if index == 0 else lane[:index] + "r" + lane[index+1:]
        track = (space*' ') + track + " /" + str(i + 1)
        tracks.append(track)
    return "\n".join(tracks)

if __name__ == '__main__':
    main()