
class SpamDetector:

    def _cleanSubjectLine(self,subjectLine):
        words = subjectLine.lower().split()

        word_data = []

        for word in words:
            data = []
            i = 0
            count = 0
        
            letter = word[0]
            while i < len(word):
                if word[i] == letter:
                    count += 1   
                else:
                    data.append(letter)
                    data.append(count)
                    count = 1
                    letter = word[i]
                i += 1
            data.append(letter)
            data.append(count)
            word_data.append(data)

            
        return word_data
        

    def _cleanKeywords(self,keywords):
        words = list(keyword.lower() for keyword in keywords)

        keyword_data = {}

        for word in words:
            data = []
            i = 0
            count = 0
                
            letter = word[0]
            while i < len(word):
                if word[i] == letter:
                    count += 1
                else:
                    data.append(letter)
                    data.append(count)
                    count = 1
                    letter = word[i]
                i += 1
            data.append(letter)
            data.append(count)            
            keyword_data[word] = data

        return keyword_data

    def countKeywords(self,subjectLine, keywords):
        subject_data = self._cleanSubjectLine(subjectLine)
        print(subject_data)
        keyword_data = self._cleanKeywords(keywords)
        print(keyword_data)

        count = 0

        for word in subject_data:
            for keyword in keyword_data:

                i = 0
                while i < len(word) - 1:
                    if keyword[i] != word[i]:
                        break
                    if keyword[i + 1] > word[i + 1]:
                        break
                    i += 2
            count += 1


        return count
            


print(SpamDetector().countKeywords("PlAyy ThEE Lottto     get Loottoo feever",["asd", "hi", "HELLO"]))