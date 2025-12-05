import React from 'react'
import { BackgroundGradientAnimation } from "@/components/ui/background-gradient-animation";
import { Translator } from '@/components/Translator'
import './App.css'

function App() {
  return (
    <BackgroundGradientAnimation>
      <Translator />
    </BackgroundGradientAnimation>
  )
}

export default App
