import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionsAnalyzer(unittest.TestCase):
    def test_emotion_detection(self):
        emotion1 = emotion_detector('I am glad this happened')
        self.assertEqual(emotion1['dominant_emotion'], 'joy')
        emotion2 = emotion_detector('I am really mad about this')
        self.assertEqual(emotion2['dominant_emotion'], 'anger')
        emotion3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(emotion3['dominant_emotion'], 'disgust')
        emotion4 = emotion_detector('I am so sad about this')
        self.assertEqual(emotion4['dominant_emotion'], 'sadness')
        emotion5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(emotion5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()