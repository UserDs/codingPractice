# by creating a new 2D array
# def RotateMatrix(N):
#     imageList1 = [[0]*N for _ in range(N)]
#     # print(imageList1) # N by N 2D array with all elemens zero
#     for i in range(0, N):
#         for j in range(0, N):
#             imageList1[i][j] = j + i * N
#     print(imageList1)
#
#     imageList2 = [[0]*N for _ in range(N)]
#     for i in range(0, N):
#         for j in range(0, N):
#             imageList2[i][j] = imageList1[N-1-j][i]
#     return imageList2



# By manuplating original 2D array
def RotateMatrix(N):
    imageList1 = [[0]*N for _ in range(N)]
    # print(imageList1) # N by N 2D array with all elemens zero
    for i in range(0, N):
        for j in range(0, N):
            imageList1[i][j] = j + i * N

    for i in range(0, int(N/2)):
        for j in range(i, N-i-1):
            # print(imageList1)
            save = imageList1[i][j]
            imageList1[i][j] = imageList1[N-j-1][i]
            # print(imageList1)
            imageList1[N-j-1][i] = imageList1[N-i-1][N-j-1]
            # print(imageList1)
            imageList1[N-i-1][N-j-1] = imageList1[j][N-i-1]
            # print(imageList1)
            imageList1[j][N-i-1] = save
            # print(imageList1)

        return imageList1


N = int(input("> "))
print(RotateMatrix(N))
