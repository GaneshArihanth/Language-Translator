import React, { useState, useEffect } from 'react';
import { Loader2 } from 'lucide-react';

export function Translator() {
    const [text, setText] = useState('');
    const [targetLang, setTargetLang] = useState('es'); // Default to Spanish
    const [translatedText, setTranslatedText] = useState('');
    const [languages, setLanguages] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000';
    console.log("Translator Component Mounted");
    console.log("API_URL:", API_URL);

    useEffect(() => {
        console.log("Fetching languages from:", `${API_URL}/api/languages`);
        fetch(`${API_URL}/api/languages`)
            .then(res => {
                console.log("Languages response status:", res.status);
                return res.json();
            })
            .then(data => {
                console.log("Languages data received:", data);
                setLanguages(data);
                if (data.length > 0) {
                    // Optional: set default to first language or keep 'es' if exists
                }
            })
            .catch(err => console.error("Failed to fetch languages:", err));
    }, []);

    const handleTranslate = async () => {
        if (!text) return;

        setLoading(true);
        setError('');
        setTranslatedText('');

        try {
            const response = await fetch(`${API_URL}/api/translate`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    text: text,
                    target_lang: targetLang,
                }),
            });

            const data = await response.json();

            if (response.ok) {
                setTranslatedText(data.translated_text);
            } else {
                setError(data.error || 'Translation failed');
            }
        } catch (err) {
            setError('Network error. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="relative z-50 flex flex-col items-center justify-center min-h-screen p-4">
            <div className="w-full max-w-2xl p-8 backdrop-blur-xl bg-white/10 border border-white/20 rounded-3xl shadow-2xl">
                <h1 className="text-4xl font-bold text-center text-white mb-8 drop-shadow-lg">
                    Language Translator
                </h1>

                <div className="space-y-6">
                    {/* Input Area */}
                    <div className="space-y-2">
                        <label className="text-white/80 text-sm font-medium ml-1">Original Text</label>
                        <textarea
                            className="w-full h-32 p-4 bg-black/20 border border-white/10 rounded-xl text-white placeholder-white/40 focus:outline-none focus:ring-2 focus:ring-white/30 resize-none transition-all"
                            placeholder="Enter text to translate..."
                            value={text}
                            onChange={(e) => setText(e.target.value)}
                        />
                    </div>

                    {/* Controls */}
                    <div className="flex flex-col md:flex-row gap-4">
                        <div className="flex-1 space-y-2">
                            <label className="text-white/80 text-sm font-medium ml-1">Target Language</label>
                            <div className="relative">
                                <select
                                    className="w-full p-3 bg-black/20 border border-white/10 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-white/30 cursor-pointer"
                                    value={targetLang}
                                    onChange={(e) => setTargetLang(e.target.value)}
                                >
                                    {languages.length === 0 && <option>Loading languages...</option>}
                                    {languages.map((lang) => (
                                        <option key={lang.id} value={lang.code} className="text-black">
                                            {lang.name}
                                        </option>
                                    ))}
                                </select>
                            </div>
                        </div>

                        <div className="flex items-end">
                            <button
                                onClick={handleTranslate}
                                disabled={loading || !text}
                                className="w-full md:w-auto px-8 py-3 bg-white/20 hover:bg-white/30 text-white font-semibold rounded-xl transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2 backdrop-blur-md border border-white/10"
                            >
                                {loading ? <Loader2 className="animate-spin h-5 w-5" /> : 'Translate'}
                            </button>
                        </div>
                    </div>

                    {/* Output Area */}
                    <div className="space-y-2">
                        <label className="text-white/80 text-sm font-medium ml-1">Translated Text</label>
                        <div className="w-full h-32 p-4 bg-white/5 border border-white/10 rounded-xl text-white/90 overflow-auto">
                            {error ? (
                                <span className="text-red-300">{error}</span>
                            ) : (
                                translatedText || <span className="text-white/30 italic">Translation will appear here...</span>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
