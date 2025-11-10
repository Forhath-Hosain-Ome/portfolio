import React from 'react';
import HeroSection from '../components/HeroSection';
import SkillSection from '../components/SkillSection';
import ProjectSection from '../components/ProjectSection';
import ContactSection from '../components/ContactSection';
import ExperienceSection from '../components/ExperienceSection';
import EducationSection from '../components/EducationSection';
import TestimonialsSection from '../components/TestimonialsSection';
import SocialLinksSection from '../components/SocialLinksSection';
import CertificatesSection from '../components/CertificatesSection';


function HomePage() {
  return (
    <>
        <HeroSection />
        <SkillSection />
        <ProjectSection />
        <ExperienceSection />
        <EducationSection />
        <TestimonialsSection />
        <CertificatesSection />
        <ContactSection />
        <SocialLinksSection />
    </>
  );
}

export default HomePage;