
def pattern1(num):
    """
    *

    * *

    * * *

    * * * *

    * * * * *
    :param num:
    :return:
    """
    for row in range(num):
        for col in range(row):
            print("*",end=" ")
        print("\n")


def pattern2(num):
    """
    * * * * * *

    * * * * *

    * * * *

    * * *

    * *

    *

    :param num:
    :return:
    """
    for row in range(num):
        for col in range(num-row):
            print("*",end=" ")
        print("\n")

def pattern3(num):
    """
              *

            * *

          * * *

        * * * *

      * * * * *

    :param num:
    :return:
    """
    for row in range(num):
        for space in range(num-row):
            print(" ", end=" ")
        for col in range(row):
            print("*",end=" ")

        print("\n")

def pattern4(num):
    """
    * * * * * *

      * * * * *

        * * * *

          * * *

            * *

              *

    :param num:
    :return:
    """
    for row in range(num):
        for space in range(row):
            print(" ", end=" ")
        for col in range(num-row):
            print("*", end=" ")
        print("\n")

def pattern5(num):
    """
    *

    * *

    * * *

    * * * *

    * * *

    * *

    *

    :param num:
    :return:
    """
    pattern1(num)
    pattern2(num)

def pattern6(num):
    """
          *

        * *

      * * *

    * * * *

      * * *

        * *

          *
    :param num:
    :return:
    """
    pattern3(num)
    pattern4(num)


def pattern7(num):
    """
          *

        *  *

      *  *  *
    :param num:
    :return:
    """
    for row in range(num):
        for space in range(num-row):
            print(" ",end=" ")
        for col in range(row):
            print("*", end=" ")
            print(" ", end=" ")
        print("\n")

def pattern8(num):
    """
    *   *   *   *

     *   *   *

      *   *

       *

    :param num:
    :return:
    """
    for row in range(num):
        for space in range(row):
            print(" ", end="")
        for col in range(num-row):
            print("*", end=" ")
            print(" ", end=" ")
        print("\n")

def pattern9(num):
    """
          *

        *   *

      *   *   *

    *   *   *   *

     *   *   *

      *   *

       *

    :param num:
    :return:
    """
    pattern7(num)
    pattern8(num)

def pattern10(num):
    """
            *

          * * *

        * * * * *

      * * * * * * *

    :param num:
    :return:
    """
    for row in range(num):
        for space in range(num-row):
            print(" ",end=" ")
        for col in range(row):
            print("*", end=" ")
        for col in range(row+1):
            print("*", end=" ")
        print("\n")

def pattern11(num):
    """
    * * * * * * *

      * * * * *

        * * *

          *
    :param num:
    :return:
    """
    for row in range(num):
        for space in range(row):
            print(" ", end=" ")
        for col in range(num-row):
            print("*",end=" ")
        for col in range(num-row-1):
            print("*",end=" ")

        print("\n")

def pattern12(num):
    """
            *

          * * *

        * * * * *

      * * * * * * *

      * * * * * * *

        * * * * *

          * * *

            *

    :param num:
    :return:
    """
    pattern10(num)
    pattern11(num)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # pattern7(4)
    pattern3(4)





