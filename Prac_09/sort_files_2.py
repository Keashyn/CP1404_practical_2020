import os


def main() :
    extension_category = {}
    os.chdir ("FilesToSort")
    for filename in os.listdir ('.') :
        if os.path.isdir (filename) :
            continue

        extension = filename.split ('.') [ -1 ]
        if extension not in extension_category :
            category = input ("In What category to sort {} files? ".format (extension))
            extension_category [ extension ] = category
            try :
                os.mkdir (category)
            except FileExistsError :
                pass
        os.rename (filename, "{}/{}".format (extension_category [ extension ], filename))


main ( )
