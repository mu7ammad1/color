import Image from "next/image";
import React from "react";
import color_hunt_logo_animation_gif from "@/app/photos/color-hunt-logo-animation.gif";

export default function Term() {
  return (
    <div
      className={`flex flex-col justify-center items-center gap-10 *:*:p-2 px-5`}
    >
      <Image
        src={color_hunt_logo_animation_gif}
        alt={`color-hunt-logo-animation.gif`}
        className={`w-52  object-cover`}
      />
      <div>
        <h1 className={`text-center font-bold`}>Terms of Service</h1>
        <p>
          Welcome to Color Hunt. By accessing or using our website, you agree to
          be bound by these Terms of Service. If you do not agree to these
          terms, you may not access or use our website.
        </p>
      </div>
      <div>
        <h1 className={`text-center font-bold`}>Limitation of Liability</h1>
        <p>
          We make no warranties or representations about the accuracy or
          completeness of the content on our website, and we are not liable for
          any damages arising from your use of our website or the content on it.
          In no event shall our company be liable for any damages whatsoever
          arising out of or in connection with the use or inability to use our
          website or the content on it.
        </p>
      </div>
      <div>
        <h1 className={`text-center font-bold`}>Indemnification</h1>
        <p>
          You agree to indemnify and hold our company, its officers, directors,
          employees, agents, and affiliates, harmless from any and all claims,
          damages, expenses, and liabilities, including reasonable attorneys&apos;
          fees, arising out of or in connection with your use of our website or
          your violation of these Terms of Service.
        </p>
      </div>
      <div>
        <h1 className={`text-center font-bold`}>Termination</h1>
        <p>
          We may terminate or suspend your access to our website, without prior
          notice or liability, for any reason whatsoever, including without
          limitation if you breach these Terms of Service.
        </p>
      </div>
      <div>
        <h1 className={`text-center font-bold`}>Changes to Terms of Service</h1>
        <p>
          We reserve the right, at our sole discretion, to modify or replace
          these Terms of Service at any time. Your continued use of our website
          after any such changes constitutes your acceptance of the new Terms of
          Service.
        </p>
      </div>
    </div>
  );
}
