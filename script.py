from PyPDF2 import PdfFileReader, PdfFileWriter


def main():
    page_offset = 13
    header_1_offset = -2

    input_pdf = PdfFileReader(
        open("asd.pdf", "rb"))
    output = PdfFileWriter()
    for i in range(439):
        output.addPage(input_pdf.getPage(i))

    header = [
        output.addBookmark(
            "Cover",
            0
        ),
        output.addBookmark(
            "Contents",
            3)
        ,
        output.addBookmark(
            "Preface",
            7
        ),
    ]

    body = [
        output.addBookmark(
            "I: The Dimensions of Reading",
            page_offset + header_1_offset + 3
        ),
        output.addBookmark(
            "II: The Third Level of Reading - Analytical Reading",
            page_offset + header_1_offset + 59
        ),
        output.addBookmark(
            "III: Approaches to Different Kinds of Reading Matter",
            page_offset + header_1_offset + 191
        ),
        output.addBookmark(
            "IV: The Ultimate Goal of Reading",
            page_offset + header_1_offset + 309
        ),
    ]

    footer = [
        output.addBookmark(
            "A: A Recommended Reading List",
            page_offset + 361
        ),
        output.addBookmark(
            "B: Exercises and Tests at the Four Level of Reading",
            page_offset + 377
        ),
    ]

    body_0 = [
        output.addBookmark(
            "1 The Activity and Art of Reading",
            page_offset + 3, body[0]
        ),
        output.addBookmark(
            "2 The Levels of Reading",
            page_offset + 16, body[0]
        ),
        output.addBookmark(
            "3 The First Level of Reading: Elementary Reading",
            page_offset + 21, body[0]
        ),
        output.addBookmark(
            "4 The Second Level of Reading: Inspectional Reading",
            page_offset + 31, body[0]
        ),
        output.addBookmark(
            "5 How to Be a Demanding Reader",
            page_offset + 45, body[0]
        ),
    ]

    child_1 = [
        output.addBookmark(
            "1.1 Active Reading",
            page_offset + 4, body_0[0]
        ),
        output.addBookmark(
            "1.2 The Goals of Reading: Reading for Information and Reading for Understanding",
            page_offset + 7, body_0[0]
        ),
        output.addBookmark(
            "1.3 Reading as Learning: The Difference Between Learning by Instruction and Learning by Discovery",
            page_offset + 11, body_0[0]
        ),
        output.addBookmark(
            "1.4 Present and Absent Teachers",
            page_offset + 14, body_0[0]),
    ]

    child_3 = [
        output.addBookmark(
            "3.1 Stages of Learning to Read",
            page_offset + 24, body_0[2]
        ),
        output.addBookmark(
            "3.2 Stages and Levels",
            page_offset + 26, body_0[2]
        ),
        output.addBookmark(
            "3.3 Higher Levels of Reading and Higher Education",
            page_offset + 28, body_0[2]),
        output.addBookmark(
            "3.4 Reading and the Democratic Ideals of Education",
            page_offset + 29, body_0[2]
        ),
    ]

    child_4 = [
        output.addBookmark(
            "4.1 Inspectional Reading I: Systematic Skimming or Pre-reading",
            page_offset + 32, body_0[3]
        ),
        output.addBookmark(
            "4.2 lnspectional Reading II: Superficial Reading",
            page_offset + 36, body_0[3]
        ),
        output.addBookmark(
            "4.3 On Reading Speeds",
            page_offset + 38, body_0[3]),
        output.addBookmark(
            "4.4 Fixations and Regressions",
            page_offset + 40, body_0[3]
        ),
        output.addBookmark(
            "4.4 The Problem of Comprehension",
            page_offset + 41, body_0[3]
        ),
        output.addBookmark(
            "4.4 Summary of Inspectional Reading",
            page_offset + 43, body_0[3]
        ),
    ]

    child_5 = [
        output.addBookmark(
            "5.1 The Essence of Active Reading: The Four Basic Questions a Reader Asks",
            page_offset + 46, body_0[4]
        ),
        output.addBookmark(
            "5.2 How to Make a Book Your Own",
            page_offset + 48, body_0[4]
        ),
        output.addBookmark(
            "5.3 The Three Kinds of Notemaking",
            page_offset + 51, body_0[4]),
        output.addBookmark(
            "5.4 Forming the Habit of Reading",
            page_offset + 52, body_0[4]
        ),
        output.addBookmark(
            "5.4 From Many Rules to One Habit",
            page_offset + 54, body_0[4]
        ),
    ]

    body_1 = [
        output.addBookmark(
            "6 Pigeonholing a Book",
            page_offset + 59, body[1]
        ),
        output.addBookmark(
            "7 X-raying a Book",
            page_offset + 75, body[1]
        ),
        output.addBookmark(
            "8 Coming to Terms with an Author",
            page_offset + 96, body[1]
        ),
        output.addBookmark(
            "9 Determining Author's Message",
            page_offset + 114, body[1]
        ),
        output.addBookmark(
            "10 Criticizing a Book Fairly",
            page_offset + 137, body[1]
        ),
        output.addBookmark(
            "11 Aggreeing or Disagreeing with an Author",
            page_offset + 152, body[1]
        ),
        output.addBookmark(
            "12 Aids to Reading",
            page_offset + 168, body[1]
        ),
    ]

    child_6 = [
        output.addBookmark(
            "6.1 The Importance of Classifying Books",
            page_offset + 60, body_1[0]
        ),
        output.addBookmark(
            "6.2 What You Can Learn from the Title of a Book",
            page_offset + 61, body_1[0]
        ),
        output.addBookmark(
            "6.3 Practical vs. Theoretical Books",
            page_offset + 65, body_1[0]
        ),
        output.addBookmark(
            "6.4 Kinds of Theoretical Books",
            page_offset + 70, body_1[0]
        ),
    ]

    child_7 = [
        output.addBookmark(
            "7.1 Of Plots and Plans: Stating the Unity of a Book",
            page_offset + 78, body_1[1]
        ),
        output.addBookmark(
            "7.2 Mastering the Multiplicity: The Art of Outlining a Book",
            page_offset + 83, body_1[1]
        ),
        output.addBookmark(
            "7.3 The Reciprocal Arts of Reading and Writing",
            page_offset + 90, body_1[1]
        ),
        output.addBookmark(
            "7.4 Discovering the Author's Intentions",
            page_offset + 92, body_1[1]
        ),
        output.addBookmark(
            "7.5 The First Stage of Analytical Reading",
            page_offset + 94, body_1[1]
        ),
    ]

    child_8 = [
        output.addBookmark(
            "8.1 Words vs. Terms",
            page_offset + 96, body_1[2]
        ),
        output.addBookmark(
            "8.2 Finding the Key Words",
            page_offset + 100, body_1[2]
        ),
        output.addBookmark(
            "8.3 Technical Words and Special Vocabularies",
            page_offset + 108, body_1[2]
        ),
        output.addBookmark(
            "8.4 Finding the Meanings",
            page_offset + 106, body_1[2]
        ),
    ]

    child_9 = [
        output.addBookmark(
            "9.1 Sentences vs. Propositions",
            page_offset + 117, body_1[3]
        ),
        output.addBookmark(
            "9.2 Finding the Key Sentences",
            page_offset + 121, body_1[3]
        ),
        output.addBookmark(
            "9.2 Finding the Propositions",
            page_offset + 124, body_1[3]
        ),
        output.addBookmark(
            "9.3 Finding the Arguments",
            page_offset + 128, body_1[3]
        ),
        output.addBookmark(
            "9.4 Finding the Solutions",
            page_offset + 135, body_1[3]
        ),
        output.addBookmark(
            "9.5 The Second Stage of Analytical Reading",
            page_offset + 136, body_1[3]
        ),
    ]

    child_10 = [
        output.addBookmark(
            "10.1 Teachability as a Virtue",
            page_offset + 189, body_1[4]
        ),
        output.addBookmark(
            "10.2 The Role of Rhetoric",
            page_offset + 140, body_1[4]
        ),
        output.addBookmark(
            "10.3 The Importance of Suspending Judgment",
            page_offset + 142, body_1[4]
        ),
        output.addBookmark(
            "10.4 The Importance of Avoiding Contentiousness",
            page_offset + 145, body_1[4]
        ),
        output.addBookmark(
            "10.5 On the Resolution of Disagreements",
            page_offset + 147, body_1[4]
        ),
    ]

    child_11 = [
        output.addBookmark(
            "11.1 Prejudice and Judgment",
            page_offset + 154, body_1[5]
        ),
        output.addBookmark(
            "11.2 Judging the Author's Soundness",
            page_offset + 156, body_1[5]
        ),
        output.addBookmark(
            "11.3 Judging the Author's Completeness",
            page_offset + 160, body_1[5]
        ),
        output.addBookmark(
            "11.4 The Third Stage of Analytical Reading",
            page_offset + 168, body_1[5]
        ),
    ]

    child_12 = [
        output.addBookmark(
            "12.1 The Role of Relevant Experience",
            page_offset + 169, body_1[6]
        ),
        output.addBookmark(
            "12.2 Other Books as Extrinsic Aids to Reading ",
            page_offset + 172, body_1[6]
        ),
        output.addBookmark(
            "12.3 How to Use Commentaries and Abstracts",
            page_offset + 174, body_1[6]
        ),
        output.addBookmark(
            "12.4 How to Use Reference Books",
            page_offset + 176, body_1[6]
        ),
        output.addBookmark(
            "12.5 How to Use a Dictionary",
            page_offset + 178, body_1[6]
        ),
        output.addBookmark(
            "12.6 How to Use an Encyclopedia",
            page_offset + 182, body_1[6]
        ),
    ]

    body_2 = [
        output.addBookmark(
            "13 How to Read Practical Books",
            page_offset + 191, body[2]
        ),
        output.addBookmark(
            "14 How to Read Imaginative Literature",
            page_offset + 203, body[2]
        ),
        output.addBookmark(
            "15 Suggestions for Reading Stories, Plays, and Poems",
            page_offset + 215, body[2]
        ),
        output.addBookmark(
            "16 How to Read History",
            page_offset + 234, body[2]
        ),
        output.addBookmark(
            "17 How to Read Science and Mathematics",
            page_offset + 255, body[2]
        ),
        output.addBookmark(
            "18 How to Read Philosophy",
            page_offset + 270, body[2]
        ),
        output.addBookmark(
            "19 How to Read Social Science",
            page_offset + 296, body[2]
        ),
    ]

    child_13 = [
        output.addBookmark(
            "13.1 The Two Kinds of Practical Books",
            page_offset + 193, body_2[0]
        ),
        output.addBookmark(
            "13.2 The Role of Persuasion",
            page_offset + 197, body_2[0]
        ),
        output.addBookmark(
            "13.3 What Does Agreement Entail in the Case of a Practical Book?",
            page_offset + 199, body_2[0]
        ),
    ]

    child_14 = [
        output.addBookmark(
            "14.1 How Not to Read Imaginative Literature",
            page_offset + 204, body_2[1]
        ),
        output.addBookmark(
            "14.2 General Rules for Reading Imaginative Literature",
            page_offset + 208, body_2[1]
        ),
    ]

    child_15 = [
        output.addBookmark(
            "15.1 How to Read Stories",
            page_offset + 217, body_2[2]
        ),
        output.addBookmark(
            "15.2 A Note About Epics",
            page_offset + 222, body_2[2]
        ),
        output.addBookmark(
            "15.3 How to Read Plays",
            page_offset + 228, body_2[2]
        ),
        output.addBookmark(
            "15.4 A Note About Tragedy",
            page_offset + 226, body_2[2]
        ),
        output.addBookmark(
            "15.5 How to Read Lyric Poetry",
            page_offset + 227, body_2[2]
        ),
    ]

    child_16 = [
        output.addBookmark(
            "16.1 The Elusiveness of Historical Facts",
            page_offset + 235, body_2[3]
        ),
        output.addBookmark(
            "16.2 Theories of History",
            page_offset + 237, body_2[3]
        ),
        output.addBookmark(
            "16.3 The Universal in History",
            page_offset + 239, body_2[3]
        ),
        output.addBookmark(
            "16.4 Questions to Ask of a Historical Book",
            page_offset + 241, body_2[3]
        ),
        output.addBookmark(
            "16.5 How to Read Biography and Autobiography",
            page_offset + 244, body_2[3]
        ),
        output.addBookmark(
            "16.5 How to Read About Current Events",
            page_offset + 248, body_2[3]
        ),
        output.addBookmark(
            "16.5 A Note on Digests",
            page_offset + 252, body_2[3]
        ),
    ]

    child_17 = [
        output.addBookmark(
            "17.1 Understanding the Scientific Enterprise",
            page_offset + 256, body_2[4]
        ),
        output.addBookmark(
            "17.2 Suggestions for Reading Classical Scientific Books",
            page_offset + 258, body_2[4]
        ),
        output.addBookmark(
            "17.3 Facing the Problem of Mathematics",
            page_offset + 260, body_2[4]
        ),
        output.addBookmark(
            "17.4 Handling the Mathematics in Scientific Books",
            page_offset + 264, body_2[4]
        ),
        output.addBookmark(
            "17.5 A Note on Popular Science",
            page_offset + 267, body_2[4]
        ),
    ]

    child_18 = [
        output.addBookmark(
            "18.1 The Questions Philosophers Ask",
            page_offset + 271, body_2[5]
        ),
        output.addBookmark(
            "18.2 Modem Philosophy and the Great Tradition",
            page_offset + 276, body_2[5]
        ),
        output.addBookmark(
            "18.3 On Philosophical Method",
            page_offset + 277, body_2[5]
        ),
        output.addBookmark(
            "18.4 On Philosophical Styles",
            page_offset + 280, body_2[5]
        ),
        output.addBookmark(
            "18.5 Hints for Reading Philosophy",
            page_offset + 285, body_2[5]
        ),
        output.addBookmark(
            "18.6 On Making Up Your Own Mind",
            page_offset + 290, body_2[5]
        ),
        output.addBookmark(
            "18.7 A Note on Theology",
            page_offset + 291, body_2[5]
        ),
        output.addBookmark(
            "18.7 How to Read \"Canonical\" Books ",
            page_offset + 298, body_2[5]
        ),
    ]

    child_19 = [
        output.addBookmark(
            "19.1 What Is Social Science?",
            page_offset + 297, body_2[6]
        ),
        output.addBookmark(
            "19.2 The Apparent Ease of Reading Social Science",
            page_offset + 299, body_2[6]
        ),
        output.addBookmark(
            "19.3 Difficulties of Reading Social Science",
            page_offset + 301, body_2[6]
        ),
        output.addBookmark(
            "19.4 Reading Social Science Literature",
            page_offset + 304, body_2[6]
        ),
    ]

    body_3 = [
        output.addBookmark(
            "20 The Fourth Level of Reading: Syntopical Reading",
            page_offset + 309, body[3]
        ),
        output.addBookmark(
            "21 Reading and the Growth of the Mind",
            page_offset + 337, body[3]
        ),
    ]

    child_20 = [
        output.addBookmark(
            "20.1 The Role of Inspection in Syntopical Reading",
            page_offset + 313, body_3[0]
        ),
        output.addBookmark(
            "20.2 The Five Steps in Syntopical Reading ",
            page_offset + 316, body_3[0]
        ),
        output.addBookmark(
            "20.3 The Need for Objectivity",
            page_offset + 323, body_3[0]
        ),
        output.addBookmark(
            "20.4 An Example of an Exercise in Syntopical Reading: The Idea of Progress",
            page_offset + 325, body_3[0]
        ),
        output.addBookmark(
            "20.5 The Syntopicon and How to Use It",
            page_offset + 329, body_3[0]
        ),
        output.addBookmark(
            "20.5 On the Principles That Underlie Syntopical Reading",
            page_offset + 333, body_3[0]
        ),
        output.addBookmark(
            "20.5 Summary of Syntopical Reading",
            page_offset + 335, body_3[0]
        ),
    ]

    child_21 = [
        output.addBookmark(
            "21.1 What Good Books Can Do for Us",
            page_offset + 338, body_3[1]
        ),
        output.addBookmark(
            "21.2 The Pyramid of Books",
            page_offset + 341, body_3[1]
        ),
        output.addBookmark(
            "21.3 The Life and Growth of the Mind",
            page_offset + 344, body_3[1]
        ),
    ]

    output_stream = open("How to Read a Book - M. J. Adler.pdf", "wb")
    output.write(output_stream)
    output_stream.close()


if __name__ == "__main__":
    main()
