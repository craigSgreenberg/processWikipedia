/* Copyright (C) 2008-2010 University of Massachusetts Amherst,
   Department of Computer Science.
   This file is part of "FACTORIE" (Factor graphs, Imperative, Extensible)
   http://factorie.cs.umass.edu, http://code.google.com/p/factorie/
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License. */

package cc.factorie.app.nlp
import java.io.File
import cc.factorie.app.strings.StringSegmenter

case class LoadPlainText(annotator:DocumentAnnotator = NoopDocumentAnnotator, documentName: String = null) extends Load with LoadDirectory {
  def fromSource(source:io.Source): Seq[Document] = Seq(annotator.process(new Document(source.mkString).setName(documentName)))
  def fromDirectory(dir:File): Seq[Document] = (for (file <- files(dir)) yield fromFile(file)).flatten
  def files(directory:File): Seq[File] = {
    if (!directory.exists) throw new Error("File "+directory+" does not exist")
    if (directory.isFile) return List(directory)
    val result = new scala.collection.mutable.ArrayBuffer[File]
    for (entry <- directory.listFiles) {
      if (entry.isFile) result += entry
      else if (entry.isDirectory) result ++= files(entry)
    }
    result
  }
}

object LoadPlainText extends LoadPlainText(annotator = NoopDocumentAnnotator, documentName = null)



object OldLoadPlainText {
  
  def fromString(name: String, contents: String): Document = new Document(contents).setName(name)
  
  @deprecated("Use fromString(String,String), and do segmentation separately.")
  def fromString(name: String, contents: String, segmentSentences: Boolean): Document =
    fromString(name, contents, if (segmentSentences) cc.factorie.app.nlp.segment.ClearSegmenter else cc.factorie.app.nlp.segment.ClearTokenizer)

  def fromString(name: String, contents: String, processor: DocumentAnnotator): Document =
    processor.process(new Document(contents).setName(name))
    
  def fromStream(name:String, stream:java.io.InputStream, encoding:String): Document = 
    new Document(scala.io.Source.fromInputStream(stream, encoding).mkString).setName(name)

  def fromFile(file: File, segmentSentences: Boolean = false): Document = {
    val string = scala.io.Source.fromFile(file).mkString
    fromString(file.getCanonicalPath, string, segmentSentences)
  }

  def fromDirectory(dir:File, segmentSentences:Boolean): Seq[Document] = {
    for (file <- files(dir)) yield fromFile(file, segmentSentences)
  }
  
  // Recursively descend directory, returning a list of files.
  // TODO This function should get moved into util/package.scala or somesuch.
  def files(directory:File): Seq[File] = {
    if (!directory.exists) throw new Error("File "+directory+" does not exist")
    if (directory.isFile) return List(directory)
    val result = new scala.collection.mutable.ArrayBuffer[File]
    for (entry <- directory.listFiles) {
      if (entry.isFile) result += entry
      else if (entry.isDirectory) result ++= files(entry)
    }
    result
  }

  
}