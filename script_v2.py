from PyPDF2 import PdfFileReader, PdfFileWriter


PAGE_OFFSET = 15


def main():
    input_pdf = PdfFileReader(
        open("asdf.pdf", "rb"))
    output = PdfFileWriter()
    for i in range(input_pdf.getNumPages()):
        output.addPage(input_pdf.getPage(i))

    bookmark_data = \
        [
            {"Cover": 0 - PAGE_OFFSET},
            {"Foreword": 8 - PAGE_OFFSET},
            {"Contents": 12 - PAGE_OFFSET},
            {"I: Algebra": [
                5,
                [
                    {"1 Numbers": [
                        5,
                        [
                            {"1.1 The integers": 5},
                            {"1.2 Rules for addition": 8},
                            {"1.3 Rules for multiplicaiton": 14},
                            {"1.4 Even and odd integers; divisibility": 22},
                            {"1.5 Rational numbers": 26},
                            {"1.6 Multiplicative inverses": 42}
                        ]
                    ]},
                    {"2: Linear Equations": [
                        53,
                        [
                            {"2.1 Equations in two unknowns": 53},
                            {"2.2 Equations in three unknowns": 57}
                        ]
                    ]},
                    {"3: Real Numbers": [
                        61,
                        [
                            {"3.1 Addition and multiplication": 61},
                            {"3.2 Real numbers: positivity": 64},
                            {"3.3 Powers and roots": 70},
                            {"3.3 Inequalities": 75}
                        ]
                    ]},
                    {"4: Quadratic Equations": 83},
                    {"Interlude: On Logic and Mathematical Expressions": [
                        93,
                        [
                            {"4.1 On reading books": 93},
                            {"4.2 Logic": 94},
                            {"4.3 Sets and elements": 99},
                            {"4.4 Notation": 99},
                        ]
                    ]}
                ]
            ]},
            {"II: Intuititive Geometry": [
                107,
                [
                    {"5: Distance and Angles": [
                        107,
                        [
                            {"5.1 Distance": 107},
                            {"5.1 Angles": 110},
                            {"5.1 The Pythagoras Theorem": 120},
                        ]
                    ]},
                    {"6: Isometries": [
                        133,
                        [
                            {"6.1 Some standard mapping of the plane": 133},
                            {"6.2 Isometries": 143},
                            {"6.3 Composition of isometries": 150},
                            {"6.4 Inverse of isometries": 155},
                            {"6.5 Characterization of isometries": 163},
                            {"6.6 Congruences": 166},
                        ]
                    ]},
                    {"7: Area of Applications": [
                        173,
                        [
                            {"7.1 Area of disc of radius r": 173},
                            {"7.2 Circumference of a circle of radius r": 180},
                        ]
                    ]},
                ]
            ]},
            {"III: Coordinate Geometry": [
                191,
                [
                    {"8: Coordinates and Geometry": [
                        191,
                        [
                            {"8.1 Coordinate systems": 191},
                            {"8.2 Distance between points": 197},
                            {"8.3 Equation of a circle": 203},
                            {"8.4 Rational points on a circle": 206},
                        ]
                    ]},
                    {"9: Operation on Points": [
                        213,
                        [
                            {"9.1 Dilations and reflection": 213},
                            {"9.2 Addition, subtraction, and the parallelogram law": 218},
                        ]
                    ]},
                    {"10: Segments, Rays, and Lines": [
                        229,
                        [
                            {"10.1 Segments": 229},
                            {"10.2 Rays": 231},
                            {"10.3 Lines": 236},
                            {"10.4 Ordinary equation for a line": 246},
                        ]
                    ]},
                    {"11: Trigonometry": [
                        249,
                        [
                            {"11.1 Radian measure": 249},
                            {"11.2 Sine and cosine": 252},
                            {"11.3 The graphs": 264},
                            {"11.4 The tangent": 266},
                            {"11.5 Addition formulas": 272},
                            {"11.6 Rotations": 277},
                        ]
                    ]},
                    {"12: Some Analytic Geometry": [
                        281,
                        [
                            {"12.1 The straight line again": 281},
                            {"12.2 The parabola": 252},
                            {"12.3 The ellipse": 264},
                            {"12.4 The hyperbola": 266},
                            {"12.5 Rotation of hyperbolas": 272},
                        ]
                    ]},
                ]
            ]},
            {"IV: Miscellaneous": [
                313,
                [
                    {"13: Functions": [
                        313,
                        [
                            {"13.1 Definition of a function": 313},
                            {"13.2 Polynomial functions": 318},
                            {"13.3 Graphs of functions": 330},
                            {"13.4 Exponential function": 333},
                            {"13.5 Logarithms": 338},
                        ]
                    ]},
                    {"14: Mappings": [
                        345,
                        [
                            {"14.1 Definition": 345},
                            {"14.2 Formalism of mappings": 351},
                            {"14.3 Permutations": 359},
                        ]
                    ]},
                    {"15: Complex Numbers": [
                        375,
                        [
                            {"15.1 The complex plane": 375},
                            {"15.2 Polar form": 380},
                        ]
                    ]},
                    {"16: Induction and Summations": [
                        383,
                        [
                            {"16.1 Induction": 383},
                            {"16.2 Summations": 388},
                            {"16.3 Geometric series": 396},
                        ]
                    ]},
                    {"17: Determinants": [
                        401,
                        [
                            {"17.1 Matrices": 401},
                            {"17.2 Determinants of order 2": 406},
                            {"17.3 Properties of 2 X 2 determinants": 409},
                            {"17.4 Determinants of order 3": 414},
                            {"17.5 Properties of 3 X 3 determinants": 418},
                            {"17.6 Cramer’s Rule": 424},
                        ]
                    ]},
                ]
            ]},
            {"Answers to Selected Exercises": 450 - PAGE_OFFSET},
        ]

    recursive_bookmarking(bookmark_data, output)

    output_stream = open("Serge Lang - Basic Mathematics.pdf", "wb")
    output.write(output_stream)
    output_stream.close()


def recursive_bookmarking(data, output, parent=None):
    if isinstance(data, list):
        for dictionary in data:
            recursive_bookmarking(dictionary, output, parent)
    else:
        for key in data:
            if isinstance(data[key], int):
                output.addBookmark(key, data[key] + PAGE_OFFSET, parent)
                print(key, data[key], parent)
                continue
            else:
                print(key, data[key][0], parent)
                recursive_bookmarking(data[key][1], output, output.addBookmark(key, data[key][0] + PAGE_OFFSET, parent))


if __name__ == "__main__":
    main()
