import { Sparkles, MapPin, Calendar, Compass } from 'lucide-react';

interface WelcomeScreenProps {
  onQuickAction: (message: string) => void;
}

export function WelcomeScreen({ onQuickAction }: WelcomeScreenProps) {
  const quickActions = [
    { icon: MapPin, text: 'Plan a weekend getaway', color: 'bg-blue-500' },
    { icon: Calendar, text: 'Find the best travel dates', color: 'bg-emerald-500' },
    { icon: Compass, text: 'Discover hidden destinations', color: 'bg-orange-500' },
  ];

  return (
    <div className="flex-1 flex items-center justify-center p-6">
      <div className="max-w-2xl w-full text-center space-y-8 animate-fadeIn">
        <div className="space-y-4">
          <div className="inline-flex items-center justify-center w-20 h-20 bg-gradient-to-br from-blue-600 to-emerald-600 rounded-3xl shadow-xl mb-2">
            <Sparkles className="w-10 h-10 text-white" />
          </div>
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 leading-tight">
            Your AI Travel Companion
          </h1>
          <p className="text-lg text-gray-600 max-w-xl mx-auto leading-relaxed">
            Let's craft your perfect journey together. From hidden gems to popular destinations,
            I'm here to help you discover and plan unforgettable experiences.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-4">
          {quickActions.map((action, index) => (
            <button
              key={index}
              onClick={() => onQuickAction(action.text)}
              className="group p-6 bg-white rounded-2xl border border-gray-200 hover:border-transparent hover:shadow-xl transition-all duration-300 text-left"
            >
              <div className={`inline-flex items-center justify-center w-12 h-12 ${action.color} rounded-xl mb-4 group-hover:scale-110 transition-transform`}>
                <action.icon className="w-6 h-6 text-white" />
              </div>
              <p className="text-gray-800 font-medium leading-snug">{action.text}</p>
            </button>
          ))}
        </div>

        <div className="pt-8">
          <p className="text-sm text-gray-500 flex items-center justify-center gap-2">
            <Sparkles className="w-4 h-4" />
            Powered by advanced AI to make travel planning effortless
          </p>
        </div>
      </div>
    </div>
  );
}