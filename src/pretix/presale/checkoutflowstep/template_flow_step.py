from django.views.generic.base import TemplateResponseMixin

from .base_checkout_flow_step import BaseCheckoutFlowStep


class TemplateFlowStep(TemplateResponseMixin, BaseCheckoutFlowStep):
    template_name = ""

    def get_context_data(self, **kwargs):
        kwargs.setdefault('step', self)
        kwargs.setdefault('event', self.event)
        kwargs.setdefault('has_prev', self.get_prev_applicable(self.request) is not None)
        kwargs.setdefault('prev_url', self.get_prev_url(self.request))
        kwargs.setdefault('checkout_flow', [
            step
            for step in self.request._checkout_flow
            if step.is_applicable(self.request)
        ])
        return kwargs