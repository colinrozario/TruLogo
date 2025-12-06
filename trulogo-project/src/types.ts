export enum RiskLevel {
    LOW = 'Low',
    MEDIUM = 'Medium',
    HIGH = 'High',
    CRITICAL = 'Critical'
}

export interface TrademarkMatch {
    name: string;
    similarityScore: number;
    classId: string;
    status: 'Registered' | 'Pending' | 'Objected' | 'Abandoned';
    owner: string;
}

export interface AnalysisResult {
    riskScore: number; // 0-100
    riskLevel: RiskLevel;
    summary: string;
    flags: string[]; // e.g., "National Emblem Misuse", "Offensive Shape"
    visualFeatures: string[];
    similarTrademarks: TrademarkMatch[];
    recommendationSummary: string;
}

export interface BrandHealthMetric {
    date: string;
    score: number;
}

export type SupportedLanguage = 'English' | 'Bahasa Indonesia' | 'Tiếng Việt' | 'Thai' | 'Malay';

export enum AppView {
    HOME = 'home',
    ANALYSIS = 'analysis',
    GENERATION = 'generation',
    DASHBOARD = 'dashboard',
    LEGAL = 'legal',
    LITERACY = 'literacy'
}
