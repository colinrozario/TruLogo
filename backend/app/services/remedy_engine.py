class RemedyEngine:
    def get_remedy(self, risk_score: float, safety_results: dict) -> dict:
        """
        Returns structured legal advice based on risk level.
        """
        
        risk_level = "Low"
        if risk_score > 75:
            risk_level = "High"
        elif risk_score > 35:
            risk_level = "Medium"
            
        advice = {}
        
        if risk_level == "Low":
            advice = {
                "status": "Safe to Proceed",
                "action": "File for Trademark (TM-A)",
                "steps": [
                    "Conduct a final comprehensive search on IP India/WIPO database.",
                    "Identify the correct NICE class for your goods/services.",
                    "File Form TM-A.",
                    "Start using the ™ symbol."
                ],
                "warning": "Even low risk does not guarantee registration. Examiners may check phonetic similarity."
            }
            
        elif risk_level == "Medium":
             advice = {
                "status": "Caution Advised",
                "action": "Consult IP Attorney & Consider Minor Redesign",
                "steps": [
                    "Review the similar marks shown below carefully.",
                    "If your logo is very similar to a registered mark in the SAME class, you must redesign.",
                    "If the similar marks are in different industries, you might be safe.",
                    "Consult a trademark attorney for a 'Search Report'."
                ],
                "warning": "Proceeding without advice may lead to opposition (Form TM-O) later."
            }
            
        else: # High
             advice = {
                "status": "High Risk - Do Not Use",
                "action": "Immediate Rebranding Required",
                "steps": [
                    "Your logo is dangerously similar to existing marks.",
                    "Using this logo could lead to 'Cease and Desist' notices or infringement lawsuits.",
                    "Use our 'Regenerate' tool to create a distinct alternative.",
                    "Do not invest in printing or signage yet."
                ],
                "warning": "High probability of application rejection under Section 9/11 of Trade Marks Act."
            }
            
        # Add safety flag specific advice
        flag_advice = []
        for flag in safety_results.get("flags", []):
            if flag["severity"] == "High":
                flag_advice.append(f"CRITICAL: {flag['message']}")
            elif flag["severity"] == "Medium":
                flag_advice.append(f"Note: {flag['message']}")
                
        if flag_advice:
            advice["specific_warnings"] = flag_advice
            
        return {
            "risk_level": risk_level,
            "advice": advice
        }

remedy_engine = RemedyEngine()
