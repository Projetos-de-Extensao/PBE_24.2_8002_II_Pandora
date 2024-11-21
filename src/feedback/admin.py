from django.contrib import admin
from .models import PlatformFeedback, FeedbackAnalysis

@admin.register(PlatformFeedback)
class PlatformFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'requester', 'submission_date')
    search_fields = ('category', 'requester__username', 'description')

@admin.register(FeedbackAnalysis)
class FeedbackAnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'feedback_id', 'feedback_description', 'status', 'analysis_date')
    readonly_fields = ('feedback_id', 'feedback_description')

    def feedback_id(self, obj):
        return obj.feedback.id
    feedback_id.short_description = "Feedback ID"

    def feedback_description(self, obj):
        return obj.feedback.description
    feedback_description.short_description = "Feedback Description"
