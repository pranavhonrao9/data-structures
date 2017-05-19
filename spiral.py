

a =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


def spiral(m,n,a):
    k=0
    l=0
    while (k<m and  l<n):

        for i in range(l, n):
            print a[k][i]
        k = k + 1

        for i in range(k, m):
            print a[i][n-1]
        n = n - 1

        if (k<m):
            for i in range(n-1,l-1,-1):
              #  print 'm-1',m-1,'i',i
                print a[m-1][i]
        m= m-1

        if (l<n):
            for i in range(m-1,k-1,-1):
                print a[i][l]
        l= l+1

temp = spiral(4,4,a)

print temp



