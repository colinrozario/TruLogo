import React from 'react';
import { Shield, Search, FileText, Activity, AlertTriangle, CheckCircle, BarChart3, Globe, UploadCloud, RefreshCw, Zap, BookOpen, Scale } from 'lucide-react';

export const NAV_ITEMS = [
    { id: 'home', label: 'Home', icon: <Shield className="w-4 h-4" /> },
    { id: 'analysis', label: 'Analyze Logo', icon: <Search className="w-4 h-4" /> },
    { id: 'generation', label: 'Regenerate', icon: <RefreshCw className="w-4 h-4" /> },
    { id: 'dashboard', label: 'Dashboard', icon: <BarChart3 className="w-4 h-4" /> },
    { id: 'literacy', label: 'IP Guide', icon: <BookOpen className="w-4 h-4" /> },
];

export const LANGUAGES = [
    { code: 'en', label: 'English' },
    { code: 'id', label: 'Bahasa Indonesia' },
    { code: 'vi', label: 'Tiếng Việt' },
    { code: 'th', label: 'Thai' },
    { code: 'ms', label: 'Malay' },
];

export const MOCK_CHART_DATA = [
    { name: 'Jan', score: 65 },
    { name: 'Feb', score: 59 },
    { name: 'Mar', score: 80 },
    { name: 'Apr', score: 81 },
    { name: 'May', score: 90 },
    { name: 'Jun', score: 95 },
];
