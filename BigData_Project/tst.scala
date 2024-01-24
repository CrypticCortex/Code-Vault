import scala.io.Source
import scala.util.matching.Regex
import scala.util.Try

object Main extends App {
  // Read the input file
  val sourceFile = "training.1600000.processed.noemoticon.csv"
  val source = Source.fromFile(sourceFile)
  val lines = source.getLines().toList
  source.close()

  // Define the column names and indices
  val DATASET_COLUMNS = List("target", "ids", "date", "flag", "user", "text")
  val targetIndex = DATASET_COLUMNS.indexOf("target")
  val textIndex = DATASET_COLUMNS.indexOf("text")

  // Process the data
  val processedData = lines.map(line => {
    val values = line.split(",", -1)
    val target = values(targetIndex)
    val text = values(textIndex)
    (target, text)
  })

  // Clean and preprocess the data
  val processedDataClean = processedData.map(x => {
    val targetClean = x._1.replaceAll("\"", "").toIntOption.getOrElse(0)
    val textClean = preprocessText(x._2)
    (targetClean, textClean)
  })

  // Filter and remove invalid data
  val cleanData = processedDataClean.filter(x => x._1 == 0 || x._1 == 4)

  // Write the clean data to a new file
  val outputFile = "cleanData.csv"
  val writer = new java.io.PrintWriter(outputFile)
  cleanData.foreach(x => writer.println(s"${x._1},${x._2}"))
  writer.close()

  println(s"Clean data has been written to $outputFile")

  // Preprocess the text data
  def preprocessText(text: String): String = {
    // Define regex patterns
    val urlPattern = """((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"""
    val userPattern = "@[^\\s]+"
    val alphaPattern = "[^a-zA-Z0-9]\\s"
    val sequencePattern = """(.)\1\1+"""
    val seqReplacePattern = """\1\1"""
    val wordLessThan2Pattern = """\b\w{1,2}\b"""

    // Remove URLs
    val textWithoutUrls = text.replaceAll(urlPattern, " ")

    // Remove usernames
    val textWithoutUsernames = textWithoutUrls.replaceAll(userPattern, " ")

    // Remove non-alphanumeric characters
    val textWithoutNonAlphanumeric = textWithoutUsernames.replaceAll(alphaPattern, " ")

    // Replace consecutive letters with two letters
    val textWithoutConsecutiveLetters = textWithoutNonAlphanumeric.replaceAll(sequencePattern, seqReplacePattern)

    // Remove words less than 2 letters
    val textWithoutShortWords = textWithoutConsecutiveLetters.replaceAll(wordLessThan2Pattern, "")

    // Remove punctuation
    val textWithoutPunctuation = textWithoutShortWords.replaceAll("""["'(),.!?\\-]""", "")

    // Convert to lowercase
    val lowercaseText = textWithoutPunctuation.toLowerCase

    // Remove extra whitespace
    val cleanedText = lowercaseText.replaceAll("""\s+""", " ").trim

    cleanedText
  }

  // Extension method to safely convert a string to an integer option
  implicit class StringToIntOption(s: String) {
    def toIntOption: Option[Int] = Try(s.toInt).toOption
  }
}
