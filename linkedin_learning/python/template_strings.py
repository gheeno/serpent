from string import Template

def main():
    str1 = "Hello {0}, this is an example of {1}".format("World!", "Template Strings")
    print(str1)

    templ = Template("Hello ${world}")
    str2 = templ.substitute(world="world!")
    print(str2)


if __name__ == "__main__":
    main()