"""All Pydantic models for agents, state, and I/O contracts."""
from __future__ import annotations
from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, Field

Channel = Literal["voice", "chat", "sms"]
Language = Literal["ar-EG", "ar-MSA", "en"]
Band = Literal["green", "yellow", "orange", "red"]

class Message(BaseModel):
    role: Literal["user", "assistant", "system", "tool"]
    content: str
    ts: datetime = Field(default_factory=datetime.utcnow)
    agent: Optional[str] = None

class PatientRef(BaseModel):
    patient_id: Optional[str] = None
    phone: Optional[str] = None
    name: Optional[str] = None
    language: Language = "ar-EG"
    consent_granted: bool = False
    consent_scope: list[str] = []

class HistoryOutput(BaseModel):
    found: bool
    patient_id: Optional[str] = None
    name: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[Literal["M", "F"]] = None
    language: Language = "ar-EG"
    conditions: list[str] = []
    allergies: list[str] = []
    medications: list[str] = []
    prior_visits: int = 0
    last_visit_date: Optional[datetime] = None
    similar_episodes: list[dict] = []
    is_returning: bool = False
    confidence: float = 1.0

class TriageOutput(BaseModel):
    risk_score: float = Field(ge=0.0, le=1.0)
    band: Band
    red_flags: list[str] = []
    next_action: Literal[
        "self_care", "schedule_routine", "schedule_urgent",
        "escalate_emergency", "need_more_info",
    ]
    explanation_ar: str
    explanation_en: str
    asked_questions: list[str] = []
    cited_chunks: list[str] = []
    confidence: float = 1.0
    requires_clinician_review: bool = False
    reasoning_trace: str = ""

class SchedulingOutput(BaseModel):
    status: Literal["booked", "options_proposed", "no_availability", "needs_escalation"]
    appointment_id: Optional[str] = None
    doctor_id: Optional[str] = None
    doctor_name: Optional[str] = None
    specialty: Optional[str] = None
    slot_start: Optional[datetime] = None
    slot_end: Optional[datetime] = None
    location: Optional[str] = None
    proposed_slots: list[dict] = []
    confidence: float = 1.0
    reasoning: str = ""

class CommunicationOutput(BaseModel):
    delivered: bool
    channel: Channel
    message_id: Optional[str] = None
    delivered_at: Optional[datetime] = None
    error: Optional[str] = None
    transcript: Optional[str] = None

class EscalationOutput(BaseModel):
    paged: bool
    clinician_id: Optional[str] = None
    clinician_name: Optional[str] = None
    specialty: Optional[str] = None
    page_method: Optional[str] = None
    acknowledged_at: Optional[datetime] = None
    acknowledgment_seconds: Optional[int] = None
    voice_bridge: Optional[dict] = None
    summary_sent: bool = False
    sla_target_seconds: int = 30
    sla_met: Optional[bool] = None
    error: Optional[str] = None

class PatientMessage(BaseModel):
    session_id: str
    channel: Channel
    phone: Optional[str] = None
    text: str
    language: Language = "ar-EG"
    audio_transcript: Optional[str] = None