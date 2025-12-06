import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
    variable: "--font-geist-sans",
    subsets: ["latin"],
});

const geistMono = Geist_Mono({
    variable: "--font-geist-mono",
    subsets: ["latin"],
});

export const metadata = {
    title: "TruLogo - AI Trademark Verification",
    description: "Protect your brand with AI-powered logo trademark analysis",
};

return (
    <html lang="en" className="dark">
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:wght@400;600;700&family=Fira+Code:wght@400&display=swap" rel="stylesheet" />
        </head>
        <body className="antialiased text-neutral-200">
            {children}
        </body>
    </html>
);
