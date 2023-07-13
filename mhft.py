import random
import datetime

class MentalHealthTracker:

    def __init__(self):
        self.mood = "neutral"
        self.sleep_quality = "average"
        self.stress_level = "low"

    def track_mood(self, mood):
        self.mood = mood

    def track_sleep_quality(self, sleep_quality):
        self.sleep_quality = sleep_quality

    def track_stress_level(self, stress_level):
        self.stress_level = stress_level

    def get_insights(self):
        insights = []
        if self.mood == "sad":
            insights.append("It's okay to not be okay.")
            insights.append("Reach out to a friend or family member for support.")
        elif self.sleep_quality == "bad":
            insights.append("Try some relaxation techniques before bed.")
            insights.append("Make sure you're getting enough exercise during the day.")
        elif self.stress_level == "high":
            insights.append("Take some time for yourself to relax.")
            insights.append("Talk to a therapist or counselor if you're feeling overwhelmed.")
        return insights

    def get_recommendations(self):
        recommendations = []
        if self.mood == "sad":
            recommendations.append("Try some meditation exercises.")
            recommendations.append("Listen to some relaxing music.")
        elif self.sleep_quality == "bad":
            recommendations.append("Go for a walk in nature.")
            recommendations.append("Read a book before bed.")
        elif self.stress_level == "high":
            recommendations.append("Try some deep breathing exercises.")
            recommendations.append("Yoga can help to reduce stress.")
        return recommendations

def main():
    tracker = MentalHealthTracker()
    tracker.track_mood("sad")
    tracker.track_sleep_quality("bad")
    tracker.track_stress_level("high")
    insights = tracker.get_insights()
    recommendations = tracker.get_recommendations()
    print("Insights:", insights)
    print("Recommendations:", recommendations)

if __name__ == "__main__":
    main()
