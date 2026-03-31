class Finding:
    VALID_RISK_LEVELS=['LOW','MEDIUM','HIGH', 'CRITICAL']

    def __init__(self,resource_type,resource_id,issue,risk_level):
        self.resource_type=resource_type
        self.resource_id=resource_id
        self.issue=issue
        self.risk_level=risk_level

    @property
    def resource_type(self):
        return self._resource_type 

    @property
    def resource_id(self):
        return self._resource_id 

    @property
    def issue(self):
        return self._issue

    @property
    def risk_level(self):
        return self._risk_level 

    @resource_type.setter
    def risk_type(self, risk_type):
        self._risk_type = risk_type 

    @resource_id.setter
    def risk_id(self, risk_id):
        self._risk_id = risk_id 

    @issue.setter
    def risk_issue(self, risk_issue):
        self._risk_issue = risk_issue 

    @risk_level.setter
    def risk_level(self, risk_level):
        if risk_level not in  Finding.VALID_RISK_LEVELS:
            raise ValueError(f"Invalid Risk Level")
        self._risk_level = risk_level 

    def __str__(self):
        return f"[{self.resource_type}] {self.resource_id} - {self.issue} {self.risk_level}"

    